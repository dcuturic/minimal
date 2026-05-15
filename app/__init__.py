from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Minimal Solutions UI Blueprints
    try:
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        from minimal_solutions.qr_code_generator.qr_code_generator_ui import ui_bp as qr_code_ui_bp
        app.register_blueprint(qr_code_ui_bp)
        
        from minimal_solutions.box_shadow_generator.box_shadow_generator_ui import ui_bp as box_shadow_ui_bp
        app.register_blueprint(box_shadow_ui_bp)
        
        from minimal_solutions.robots_txt_generator.robots_txt_generator_ui import ui_bp as robots_txt_ui_bp
        app.register_blueprint(robots_txt_ui_bp)
        
        from minimal_solutions.impressum_generator_demo.impressum_generator_demo_ui import ui_bp as impressum_generator_demo_ui_bp
        app.register_blueprint(impressum_generator_demo_ui_bp)
        
        from minimal_solutions.datenschutz_text_demo.datenschutz_text_demo_api import api_bp as datenschutz_text_demo_api_bp
        app.register_blueprint(datenschutz_text_demo_api_bp)
        
        from minimal_solutions.rechnungsnummer_generator.rechnungsnummer_generator_api import api_bp as rechnungsnummer_generator_api_bp
        app.register_blueprint(rechnungsnummer_generator_api_bp)
        
        from minimal_solutions.iban_formatter.iban_formatter_api import api_bp as iban_formatter_api_bp
        app.register_blueprint(iban_formatter_api_bp)
        
        from minimal_solutions.iban_formatter.iban_formatter_ui import ui_bp as iban_formatter_ui_bp
        app.register_blueprint(iban_formatter_ui_bp)
        
        from minimal_solutions.mwst_rechner.mwst_rechner_api import api_bp as mwst_rechner_api_bp
        app.register_blueprint(mwst_rechner_api_bp)
        
        from minimal_solutions.markdown_preview.markdown_preview_ui import ui_bp as markdown_preview_ui_bp
        app.register_blueprint(markdown_preview_ui_bp)
        
        from minimal_solutions.markdown_preview.markdown_preview_api import api_bp as markdown_preview_api_bp
        app.register_blueprint(markdown_preview_api_bp)
        
        from minimal_solutions.jwt_decoder_demo.jwt_decoder_demo_ui import ui_bp as jwt_decoder_demo_ui_bp
        app.register_blueprint(jwt_decoder_demo_ui_bp)
        
        from minimal_solutions.jwt_decoder_demo.jwt_decoder_demo_api import api_bp as jwt_decoder_demo_api_bp
        app.register_blueprint(jwt_decoder_demo_api_bp)
        
        from minimal_solutions.random_name_generator.random_name_generator_api import api_bp as random_name_generator_api_bp
        app.register_blueprint(random_name_generator_api_bp)
        
        from minimal_solutions.random_name_generator.random_name_generator_ui import ui_bp as random_name_generator_ui_bp
        app.register_blueprint(random_name_generator_ui_bp)
        
        from minimal_solutions.case_converter.case_converter_api import api_bp as case_converter_api_bp
        app.register_blueprint(case_converter_api_bp)
        
        from minimal_solutions.altersrechner.altersrechner_api import api_bp as altersrechner_api_bp
        app.register_blueprint(altersrechner_api_bp)
        
        from minimal_solutions.datumsdifferenz_rechner.datumsdifferenz_rechner_api import api_bp as datumsdifferenz_rechner_api_bp
        app.register_blueprint(datumsdifferenz_rechner_api_bp)
        
        from minimal_solutions.datumsdifferenz_rechner.datumsdifferenz_rechner_ui import ui_bp as datumsdifferenz_rechner_ui_bp
        app.register_blueprint(datumsdifferenz_rechner_ui_bp)
        
        from minimal_solutions.countdown_generator.countdown_generator_api import api_bp as countdown_generator_api_bp
        app.register_blueprint(countdown_generator_api_bp)
        
        from minimal_solutions.countdown_generator.countdown_generator_ui import ui_bp as countdown_generator_ui_bp
        app.register_blueprint(countdown_generator_ui_bp)
        
        from minimal_solutions.kontaktkarten_generator.kontaktkarten_generator_api import api_bp as kontaktkarten_generator_api_bp
        app.register_blueprint(kontaktkarten_generator_api_bp)
        
        from minimal_solutions.vcard_generator.vcard_generator_api import api_bp as vcard_generator_api_bp
        app.register_blueprint(vcard_generator_api_bp)
        
        from minimal_solutions.vcard_generator.vcard_generator_ui import ui_bp as vcard_generator_ui_bp
        app.register_blueprint(vcard_generator_ui_bp)
        
        from minimal_solutions.favicon_generator_demo.favicon_generator_demo_ui import ui_bp as favicon_generator_demo_ui_bp
        app.register_blueprint(favicon_generator_demo_ui_bp)
        
        from minimal_solutions.favicon_generator_demo.favicon_generator_demo_api import api_bp as favicon_generator_demo_api_bp
        app.register_blueprint(favicon_generator_demo_api_bp)
        
        from minimal_solutions.changelog_generator.changelog_generator_api import api_bp as changelog_generator_api_bp
        app.register_blueprint(changelog_generator_api_bp)
        
        from minimal_solutions.changelog_generator.changelog_generator_ui import ui_bp as changelog_generator_ui_bp
        app.register_blueprint(changelog_generator_ui_bp)

        from minimal_solutions.release_notes_generator.release_notes_generator_api import api_bp as release_notes_generator_api_bp
        app.register_blueprint(release_notes_generator_api_bp)
        
        from minimal_solutions.api_key_masker.api_key_masker_api import api_bp as api_key_masker_api_bp
        app.register_blueprint(api_key_masker_api_bp)

        from minimal_solutions.env_file_viewer.env_file_viewer_api import api_bp as env_file_viewer_api_bp
        app.register_blueprint(env_file_viewer_api_bp)

        from minimal_solutions.docker_compose_service_viewer.docker_compose_service_viewer_api import api_bp as docker_compose_service_viewer_api_bp
        app.register_blueprint(docker_compose_service_viewer_api_bp)

        from minimal_solutions.port_checker_demo.port_checker_demo_ui import ui_bp as port_checker_demo_ui_bp
        app.register_blueprint(port_checker_demo_ui_bp)

        from minimal_solutions.error_message_explainer.error_message_explainer_api import api_bp as error_message_explainer_api_bp
        app.register_blueprint(error_message_explainer_api_bp)

        from minimal_solutions.error_message_explainer.error_message_explainer_ui import ui_bp as error_message_explainer_ui_bp
        app.register_blueprint(error_message_explainer_ui_bp)

        from minimal_solutions.faq_generator.faq_generator_ui import ui_bp as faq_generator_ui_bp
        app.register_blueprint(faq_generator_ui_bp)

        from minimal_solutions.faq_generator.faq_generator_api import api_bp as faq_generator_api_bp
        app.register_blueprint(faq_generator_api_bp)

        from minimal_solutions.knowledge_base_card_generator.knowledge_base_card_generator_api import api_bp as knowledge_base_card_generator_api_bp
        app.register_blueprint(knowledge_base_card_generator_api_bp)

        from minimal_solutions.website_health_check_demo.website_health_check_demo_api import api_bp as website_health_check_demo_api_bp
        app.register_blueprint(website_health_check_demo_api_bp)

        from minimal_solutions.uptime_badge_generator.uptime_badge_generator_ui import ui_bp as uptime_badge_generator_ui_bp
        app.register_blueprint(uptime_badge_generator_ui_bp)
        from minimal_solutions.uptime_badge_generator.uptime_badge_generator_api import api_bp as uptime_badge_generator_api_bp
        app.register_blueprint(uptime_badge_generator_api_bp)

        from minimal_solutions.server_resource_card_demo.server_resource_card_demo_api import api_bp as server_resource_card_demo_api_bp
        app.register_blueprint(server_resource_card_demo_api_bp)

        from minimal_solutions.docker_container_card_demo.docker_container_card_demo_api import api_bp as docker_container_card_demo_api_bp
        app.register_blueprint(docker_container_card_demo_api_bp)

        from minimal_solutions.minecraft_motd_preview.minecraft_motd_preview_ui import ui_bp as minecraft_motd_preview_ui_bp
        app.register_blueprint(minecraft_motd_preview_ui_bp)

        from minimal_solutions.minecraft_motd_preview.minecraft_motd_preview_api import api_bp as minecraft_motd_preview_api_bp
        app.register_blueprint(minecraft_motd_preview_api_bp)

        from minimal_solutions.subdomain_generator.subdomain_generator_api import api_bp as subdomain_generator_api_bp
        app.register_blueprint(subdomain_generator_api_bp)

        from minimal_solutions.dns_record_builder.dns_record_builder_ui import ui_bp as dns_record_builder_ui_bp
        app.register_blueprint(dns_record_builder_ui_bp)

        from minimal_solutions.dns_record_builder.dns_record_builder_api import api_bp as dns_record_builder_api_bp
        app.register_blueprint(dns_record_builder_api_bp)

        from minimal_solutions.ssl_expiry_checker_demo.ssl_expiry_checker_demo_api import api_bp as ssl_expiry_checker_demo_api_bp
        app.register_blueprint(ssl_expiry_checker_demo_api_bp)

        from minimal_solutions.backup_plan_generator.backup_plan_generator_api import api_bp as backup_plan_generator_api_bp
        app.register_blueprint(backup_plan_generator_api_bp)

        from minimal_solutions.maintenance_page_generator.maintenance_page_generator_ui import ui_bp as maintenance_page_generator_ui_bp
        app.register_blueprint(maintenance_page_generator_ui_bp)

        from minimal_solutions.status_page_incident_generator.status_page_incident_generator_ui import ui_bp as status_page_incident_generator_ui_bp
        app.register_blueprint(status_page_incident_generator_ui_bp)

        from minimal_solutions.status_page_incident_generator.status_page_incident_generator_api import api_bp as status_page_incident_generator_api_bp
        app.register_blueprint(status_page_incident_generator_api_bp)

        from minimal_solutions.curl_command_generator.curl_command_generator_api import api_bp as curl_command_generator_api_bp
        app.register_blueprint(curl_command_generator_api_bp)

        from minimal_solutions.openapi_endpoint_stub_generator.openapi_endpoint_stub_generator_api import api_bp as openapi_endpoint_stub_generator_api_bp
        app.register_blueprint(openapi_endpoint_stub_generator_api_bp)

        from minimal_solutions.json_schema_validator_demo.json_schema_validator_demo_ui import ui_bp as json_schema_validator_demo_ui_bp
        app.register_blueprint(json_schema_validator_demo_ui_bp)

        from minimal_solutions.json_schema_validator_demo.json_schema_validator_demo_api import api_bp as json_schema_validator_demo_api_bp
        app.register_blueprint(json_schema_validator_demo_api_bp)

        from minimal_solutions.access_role_matrix_demo.access_role_matrix_demo_ui import ui_bp as access_role_matrix_demo_ui_bp
        app.register_blueprint(access_role_matrix_demo_ui_bp)

        from minimal_solutions.access_role_matrix_demo.access_role_matrix_demo_api import api_bp as access_role_matrix_demo_api_bp
        app.register_blueprint(access_role_matrix_demo_api_bp)

        from minimal_solutions.feature_flag_panel_demo.feature_flag_panel_demo_ui import ui_bp as feature_flag_panel_demo_ui_bp
        app.register_blueprint(feature_flag_panel_demo_ui_bp)

        from minimal_solutions.feature_flag_panel_demo.feature_flag_panel_demo_api import api_bp as feature_flag_panel_demo_api_bp
        app.register_blueprint(feature_flag_panel_demo_api_bp)

        from minimal_solutions.component_preview_card.component_preview_card_ui import ui_bp as component_preview_card_ui_bp
        app.register_blueprint(component_preview_card_ui_bp)

        from minimal_solutions.component_preview_card.component_preview_card_api import api_bp as component_preview_card_api_bp
        app.register_blueprint(component_preview_card_api_bp)

        from minimal_solutions.component_json_builder.component_json_builder_ui import ui_bp as component_json_builder_ui_bp
        app.register_blueprint(component_json_builder_ui_bp)

        from minimal_solutions.component_json_builder.component_json_builder_api import api_bp as component_json_builder_api_bp
        app.register_blueprint(component_json_builder_api_bp)

        from minimal_solutions.html_fragment_wrapper.html_fragment_wrapper_ui import ui_bp as html_fragment_wrapper_ui_bp
        app.register_blueprint(html_fragment_wrapper_ui_bp)

        from minimal_solutions.html_fragment_wrapper.html_fragment_wrapper_api import api_bp as html_fragment_wrapper_api_bp
        app.register_blueprint(html_fragment_wrapper_api_bp)

        from minimal_solutions.iframe_preview_url_builder.iframe_preview_url_builder_ui import ui_bp as iframe_preview_url_builder_ui_bp
        app.register_blueprint(iframe_preview_url_builder_ui_bp)

        from minimal_solutions.iframe_preview_url_builder.iframe_preview_url_builder_api import api_bp as iframe_preview_url_builder_api_bp
        app.register_blueprint(iframe_preview_url_builder_api_bp)

        from minimal_solutions.decision_log_generator.decision_log_generator_ui import ui_bp as decision_log_generator_ui_bp
        app.register_blueprint(decision_log_generator_ui_bp)

        from minimal_solutions.decision_log_generator.decision_log_generator_api import api_bp as decision_log_generator_api_bp
        app.register_blueprint(decision_log_generator_api_bp)

        from minimal_solutions.pricing_table_generator.pricing_table_generator_api import api_bp as pricing_table_generator_api_bp
        app.register_blueprint(pricing_table_generator_api_bp)

        from minimal_solutions.pricing_table_generator.pricing_table_generator_ui import ui_bp as pricing_table_generator_ui_bp
        app.register_blueprint(pricing_table_generator_ui_bp)

        from minimal_solutions.testimonial_card_generator.testimonial_card_generator_api import api_bp as testimonial_card_generator_api_bp
        app.register_blueprint(testimonial_card_generator_api_bp)

        from minimal_solutions.social_post_formatter.social_post_formatter_api import api_bp as social_post_formatter_api_bp
        app.register_blueprint(social_post_formatter_api_bp)

        from minimal_solutions.youtube_description_generator.youtube_description_generator_api import api_bp as youtube_description_generator_api_bp
        app.register_blueprint(youtube_description_generator_api_bp)

        from minimal_solutions.image_prompt_generator.image_prompt_generator_api import api_bp as image_prompt_generator_api_bp
        app.register_blueprint(image_prompt_generator_api_bp)

        from minimal_solutions.prompt_template_builder.prompt_template_builder_api import api_bp as prompt_template_builder_api_bp
        app.register_blueprint(prompt_template_builder_api_bp)

        from minimal_solutions.landingpage_converter.landingpage_converter_api import api_bp as landingpage_converter_api_bp
        app.register_blueprint(landingpage_converter_api_bp)

        from minimal_solutions.landingpage_viewer.landingpage_viewer_ui import ui_bp as landingpage_viewer_ui_bp
        app.register_blueprint(landingpage_viewer_ui_bp)

        from minimal_solutions.landingpage_viewer.landingpage_viewer_api import api_bp as landingpage_viewer_api_bp
        app.register_blueprint(landingpage_viewer_api_bp)

        from minimal_solutions.landingpage_exporter.landingpage_exporter_api import api_bp as landingpage_exporter_api_bp
        app.register_blueprint(landingpage_exporter_api_bp)

        from minimal_solutions.landingpage_importer.landingpage_importer_api import api_bp as landingpage_importer_api_bp
        app.register_blueprint(landingpage_importer_api_bp)

        from minimal_solutions.landingpage_masker.landingpage_masker_api import api_bp as landingpage_masker_api_bp
        app.register_blueprint(landingpage_masker_api_bp)

        from minimal_solutions.landingpage_splitter.landingpage_splitter_api import api_bp as landingpage_splitter_api_bp
        app.register_blueprint(landingpage_splitter_api_bp)

        from minimal_solutions.landingpage_merger.landingpage_merger_api import api_bp as landingpage_merger_api_bp
        app.register_blueprint(landingpage_merger_api_bp)

        from minimal_solutions.landingpage_cleaner.landingpage_cleaner_api import api_bp as landingpage_cleaner_api_bp
        app.register_blueprint(landingpage_cleaner_api_bp)

        from minimal_solutions.landingpage_normalizer.landingpage_normalizer_ui import ui_bp as landingpage_normalizer_ui_bp
        app.register_blueprint(landingpage_normalizer_ui_bp)

        from minimal_solutions.landingpage_normalizer.landingpage_normalizer_api import api_bp as landingpage_normalizer_api_bp
        app.register_blueprint(landingpage_normalizer_api_bp)

        from minimal_solutions.landingpage_diff_viewer.landingpage_diff_viewer_ui import ui_bp as landingpage_diff_viewer_ui_bp
        app.register_blueprint(landingpage_diff_viewer_ui_bp)

        from minimal_solutions.landingpage_diff_viewer.landingpage_diff_viewer_api import api_bp as landingpage_diff_viewer_api_bp
        app.register_blueprint(landingpage_diff_viewer_api_bp)

        from minimal_solutions.landingpage_template_builder.landingpage_template_builder_api import api_bp as landingpage_template_builder_api_bp
        app.register_blueprint(landingpage_template_builder_api_bp)

        from minimal_solutions.seo_formatter.seo_formatter_api import api_bp as seo_formatter_api_bp
        app.register_blueprint(seo_formatter_api_bp)

        from minimal_solutions.seo_formatter.seo_formatter_ui import ui_bp as seo_formatter_ui_bp
        app.register_blueprint(seo_formatter_ui_bp)

        from minimal_solutions.seo_validator.seo_validator_api import api_bp as seo_validator_api_bp
        app.register_blueprint(seo_validator_api_bp)

        from minimal_solutions.seo_masker.seo_masker_api import api_bp as seo_masker_api_bp
        app.register_blueprint(seo_masker_api_bp)

        from minimal_solutions.seo_splitter.seo_splitter_api import api_bp as seo_splitter_api_bp
        app.register_blueprint(seo_splitter_api_bp)

        from minimal_solutions.seo_merger.seo_merger_api import api_bp as seo_merger_api_bp
        app.register_blueprint(seo_merger_api_bp)

        from minimal_solutions.seo_normalizer.seo_normalizer_api import api_bp as seo_normalizer_api_bp
        app.register_blueprint(seo_normalizer_api_bp)

        from minimal_solutions.hosting_validator.api import api_bp as hosting_validator_api_bp
        app.register_blueprint(hosting_validator_api_bp)

        from minimal_solutions.hosting_builder.api_hosting_builder import api_bp as hosting_builder_api_bp
        app.register_blueprint(hosting_builder_api_bp)

        from minimal_solutions.hosting_converter.api_hosting_converter import api_bp as hosting_converter_api_bp
        app.register_blueprint(hosting_converter_api_bp)

        from minimal_solutions.hosting_analyzer.api_hosting_analyzer import api_bp as hosting_analyzer_api_bp
        app.register_blueprint(hosting_analyzer_api_bp)

        from minimal_solutions.hosting_analyzer.ui_hosting_analyzer import ui_bp as hosting_analyzer_ui_bp
        app.register_blueprint(hosting_analyzer_ui_bp)

        from minimal_solutions.hosting_exporter.api_hosting_exporter import api_bp as hosting_exporter_api_bp
        app.register_blueprint(hosting_exporter_api_bp)

        from minimal_solutions.hosting_importer.api_hosting_importer import api_bp as hosting_importer_api_bp
        app.register_blueprint(hosting_importer_api_bp)

        from minimal_solutions.hosting_cleaner.api_hosting_cleaner import api_bp as hosting_cleaner_api_bp
        app.register_blueprint(hosting_cleaner_api_bp)

        from minimal_solutions.hosting_cleaner.ui_hosting_cleaner import ui_bp as hosting_cleaner_ui_bp
        app.register_blueprint(hosting_cleaner_ui_bp)

        from minimal_solutions.hosting_template_builder.api_hosting_template_builder import api_hosting_template_builder_bp as hosting_template_builder_api_bp
        app.register_blueprint(hosting_template_builder_api_bp)

        try:
            from minimal_solutions.hosting_template_builder.ui_hosting_template_builder import ui_bp as hosting_template_builder_ui_bp
            app.register_blueprint(hosting_template_builder_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_generator.api_minecraft_generator import api_bp as minecraft_generator_api_bp
            app.register_blueprint(minecraft_generator_api_bp)
            from minimal_solutions.minecraft_generator.ui_minecraft_generator import ui_bp as minecraft_generator_ui_bp
            app.register_blueprint(minecraft_generator_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_formatter.api_minecraft_formatter import api_bp as minecraft_formatter_api_bp
            app.register_blueprint(minecraft_formatter_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_validator.api_minecraft_validator import api_bp as minecraft_validator_api_bp
            app.register_blueprint(minecraft_validator_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_preview.minecraft_preview_ui import ui_bp as minecraft_preview_ui_bp
            app.register_blueprint(minecraft_preview_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_preview.api import api_bp as minecraft_preview_api_bp
            app.register_blueprint(minecraft_preview_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_builder.api_minecraft_builder import api_bp as minecraft_builder_api_bp
            app.register_blueprint(minecraft_builder_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_converter.api_minecraft_converter import api_bp as minecraft_converter_api_bp
            app.register_blueprint(minecraft_converter_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_converter.minecraft_converter_ui import ui_bp as minecraft_converter_ui_bp
            app.register_blueprint(minecraft_converter_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_analyzer.api_minecraft_analyzer import api_bp as minecraft_analyzer_api_bp
            app.register_blueprint(minecraft_analyzer_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_analyzer.minecraft_analyzer_ui import ui_bp as minecraft_analyzer_ui_bp
            app.register_blueprint(minecraft_analyzer_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_summarizer.api_minecraft_summarizer import api_bp as minecraft_summarizer_api_bp
            app.register_blueprint(minecraft_summarizer_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_summarizer.minecraft_summarizer_ui import ui_bp as minecraft_summarizer_ui_bp
            app.register_blueprint(minecraft_summarizer_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_checker.api_minecraft_checker import api_bp as minecraft_checker_api_bp
            app.register_blueprint(minecraft_checker_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_checker.minecraft_checker_ui import ui_bp as minecraft_checker_ui_bp
            app.register_blueprint(minecraft_checker_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_viewer.minecraft_viewer_api import api_bp as minecraft_viewer_api_bp
            app.register_blueprint(minecraft_viewer_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_viewer.minecraft_viewer_ui import ui_bp as minecraft_viewer_ui_bp
            app.register_blueprint(minecraft_viewer_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_importer.minecraft_importer_api import api_bp as minecraft_importer_api_bp
            app.register_blueprint(minecraft_importer_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_importer.minecraft_importer_ui import ui_bp as minecraft_importer_ui_bp
            app.register_blueprint(minecraft_importer_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_masker.minecraft_masker_api import api_bp as minecraft_masker_api_bp
            app.register_blueprint(minecraft_masker_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_masker.minecraft_masker_ui import ui_bp as minecraft_masker_ui_bp
            app.register_blueprint(minecraft_masker_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_splitter.minecraft_splitter_api import api_bp as minecraft_splitter_api_bp
            app.register_blueprint(minecraft_splitter_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_splitter.minecraft_splitter_ui import ui_bp as minecraft_splitter_ui_bp
            app.register_blueprint(minecraft_splitter_ui_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_merger.minecraft_merger_api import api_bp as minecraft_merger_api_bp
            app.register_blueprint(minecraft_merger_api_bp)
        except ImportError:
            pass

        try:
            from minimal_solutions.minecraft_merger.minecraft_merger_ui import ui_bp as minecraft_merger_ui_bp
            app.register_blueprint(minecraft_merger_ui_bp)
        except ImportError:
            pass

    except ImportError as e:
        print(f"Warning: Could not import UI blueprints: {e}")
        
    return app
