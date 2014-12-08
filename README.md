CIS4301-Project-GUL
===================

Gainesville Utilities Lookup, project for CIS4301.

A Nice Workflow
----------

* Create a new branch (from master usually) for a feature

``` git checkout -b newbranch ```
* Implement the feature on this branch
* When done implementing make a github Pull Request to merge it back in
*If there is not more work to do or no point in keeping it,
    delete the branch, too

[Workflow](https://guides.github.com/introduction/flow/index.html)

* The data: 
* Energy consumption by service address - https://data.cityofgainesville.org/Environment-Energy/Electric-Consumption-By-Service-Address/jp78-igic
* Energy consumption by month - https://data.cityofgainesville.org/Environment-Energy/Electric-Consumption-By-Month/7dsc-hrh4

## Queries

### Query 1

// Gets the average electricity usage for a specific month

Select AVG(ElectricityReport.Usage) as avgMonthEnergy
From ElectricityReport
Where Month = “STRING OF THE MONTH”

### Query 2

// Gets the overall average water usage

Select AVG(Usage) as avgTotalWater
From WaterReport

### Query 3

//Gets the average water usage for a specific address

Select AVG(WaterReport.Usage) as avgHouseWater
From WaterReport, Address
Where WaterReport.address.ID = Address.ID

### Query 4

//Gets the average water usage for a specific month

Select AVG(WaterReport.Usage) as avgMonthWater
From WaterReport
Where Month = “STRING OF THE MONTH”

### Query 5

//Gets the address of any households that had the same amount of electricity and water usage in a month

Select StreetAddress
From Address, ElectricityReport, WaterReport
Where WaterReport.ID = Address.ID 
AND ElectricityReport.ID = Address.ID
AND ElectricityReport.Usage = WaterReport.Usage
AND WaterReport.Month = ElectricityReport.Month
* Energy consumption by service address (GRU) - https://data.cityofgainesville.org/Environment-Energy/GRU-Customer-Electric-Consumption/gk3k-9435
* Energy consumption by month - https://data.cityofgainesville.org/Environment-Energy/Electric-Consumption-By-Month/7dsc-hrh4
