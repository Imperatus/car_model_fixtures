# Car Model Fixtures
Popular car makes and models by continent and year.

## Description

Aims to add popular continental car models by continent and year for realistic test data in the mobility sector

## Getting Started

### Dependencies

* Python 3

### Installing

* pip install car_model_fixtures

### Usage

```python
from car_model_fixtures.generate import FixtureGenerator, Continent

generator = FixtureGenerator()
fixtures = generator.generate(amount=1, continent=Continent.EUROPE, year=2023)
for fixture in fixtures:
    print(fixture['brand'], fixture['model'])
```

Result:
```
> Audi A1
```

## Help

Currently we only support European continent and various popular models from the 
year 2023. We aim to add more continents and models in the future.

For excellent US car test data we can recommend the following `faker` plugin: `faker_vehicle`

## Authors

[Jurgen Buisman @ github](https://github.com/Imperatus)

## Version History

* 0.1.0
    * Initial Release with European car models from 2023

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
