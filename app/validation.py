import re

class ValidationErrors:
    REQUIRED = "Das Feld '{field}' ist ein Pflichtfeld und darf nicht leer sein."
    TYPE = "Das Feld '{field}' muss vom Typ '{type}' sein."
    MIN_LENGTH = "Das Feld '{field}' muss mindestens {min} Zeichen lang sein."
    MAX_LENGTH = "Das Feld '{field}' darf maximal {max} Zeichen lang sein."
    FORMAT = "Das Feld '{field}' entspricht nicht dem erwarteten Format ({format_name})."

class Validator:
    @staticmethod
    def check_required(value, field_name):
        if value is None or (isinstance(value, str) and not value.strip()):
            return ValidationErrors.REQUIRED.format(field=field_name)
        return None

    @staticmethod
    def check_type(value, expected_type, field_name, type_name=None):
        if value is not None and not isinstance(value, expected_type):
            t_name = type_name or expected_type.__name__
            return ValidationErrors.TYPE.format(field=field_name, type=t_name)
        return None

    @staticmethod
    def check_length(value, field_name, min_len=None, max_len=None):
        if value is None:
            return None
        length = len(str(value))
        if min_len is not None and length < min_len:
            return ValidationErrors.MIN_LENGTH.format(field=field_name, min=min_len)
        if max_len is not None and length > max_len:
            return ValidationErrors.MAX_LENGTH.format(field=field_name, max=max_len)
        return None

    @staticmethod
    def check_format(value, field_name, pattern, format_name="gültiges Format"):
        if value is None or not isinstance(value, str):
            return None
        if not re.match(pattern, value):
            return ValidationErrors.FORMAT.format(field=field_name, format_name=format_name)
        return None

    @classmethod
    def validate(cls, data, rules):
        """
        Validates a dictionary of data against a set of rules.
        rules format:
        {
            "username": {
                "required": True,
                "type": str,
                "min_length": 3,
                "max_length": 20,
                "format": (r'^[a-zA-Z0-9_]+$', "Alphanumerisch mit Unterstrich")
            }
        }
        Returns: (is_valid, errors_dict)
        """
        errors = {}
        if not isinstance(data, dict):
            return False, {"_global": ["Erwartet wurde ein JSON-Objekt/Dictionary."]}

        for field, field_rules in rules.items():
            value = data.get(field)
            field_errors = []

            # 1. Required
            if field_rules.get("required"):
                err = cls.check_required(value, field)
                if err:
                    field_errors.append(err)
                    errors[field] = field_errors
                    continue # Skip other checks if required fails
            
            if value is None or (isinstance(value, str) and not value.strip() and not field_rules.get("required")):
                continue

            # 2. Type
            if "type" in field_rules:
                err = cls.check_type(value, field_rules["type"], field, field_rules.get("type_name"))
                if err:
                    field_errors.append(err)
                    errors[field] = field_errors
                    continue

            # 3. Length
            min_len = field_rules.get("min_length")
            max_len = field_rules.get("max_length")
            if min_len is not None or max_len is not None:
                err = cls.check_length(value, field, min_len, max_len)
                if err:
                    field_errors.append(err)

            # 4. Format
            if "format" in field_rules:
                pattern, format_name = field_rules["format"]
                err = cls.check_format(value, field, pattern, format_name)
                if err:
                    field_errors.append(err)

            if field_errors:
                errors[field] = field_errors

        return len(errors) == 0, errors
