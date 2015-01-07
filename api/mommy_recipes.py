from model_mommy.recipe import Recipe, seq
from contracts.models import Contract
from itertools import cycle

SCHEDULES = ('MOBIS', 'PES')
piid = seq('123')
contract_recipe = Recipe(
        Contract,
        idv_piid=seq('ABC123'),
        piid=piid,
        vendor_name=seq("CompanyName"),
        labor_category="Legal Services",
        schedule=cycle(SCHEDULES),
        min_years_experience=seq(5),
        hourly_rate_year1=seq('2'),
        current_price=seq('2')
)

