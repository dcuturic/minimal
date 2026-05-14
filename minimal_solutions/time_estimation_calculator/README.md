# Time Estimation Calculator

The **Time Estimation Calculator** is a minimal solution designed to help teams and project managers quickly determine the feasibility of completing a set number of tickets within a given timeframe. It calculates the total required hours based on the average time per ticket, compares it against the available capacity determined by the number of workers and days, and provides a clear breakdown of utilization and feasibility.

## Features

- **Capacity Planning:** Calculates total hours available based on working days and team size (assuming an 8-hour workday).
- **Workload Estimation:** Determines the total hours required for a specific number of tickets.
- **Feasibility Check:** Instantly shows whether the workload can be completed within the available time.
- **Utilization Tracking:** Provides the resource utilization percentage.

## API Usage

The Time Estimation Calculator can be accessed programmatically via its REST API. 

### Endpoint

**POST** `/api/minimal-solutions/time_estimation_calculator`

### Request Example

```json
{
  "ticket_count": 50,
  "minutes_per_ticket": 60,
  "days": 14,
  "workers": 2
}
```

### Response Example

```json
{
  "status": "success",
  "data": {
    "total_hours_required": 50.0,
    "total_hours_available": 224.0,
    "is_feasible": true,
    "utilization_percent": 22.32
  }
}
```

## Integration

You can easily integrate this tool into your own project management dashboards, CLI tools, or CI/CD pipelines to validate sprint scopes and team capacity allocations automatically.
