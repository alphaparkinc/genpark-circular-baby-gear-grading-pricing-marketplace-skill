from client import CircularBabyGearGradingPricingMarketplaceClient

def main():
    client = CircularBabyGearGradingPricingMarketplaceClient()
    res = client.grade_and_value_baby_gear('Nuna Rava Convertible Car Seat', 650.0, 'excellent')
    print('Model: ' + res['gear_model'] + ' (' + res['algorithmic_condition_grade'] + ')')
    print('Resale Price: CAD $' + str(res['rev_algorithm_resale_cad']) + ' | Instant Payout: CAD $' + str(res['instant_payout_offer_cad']))
    print('Safety Recalls Cleared: ' + str(res['safety_recall_registry_cleared']) + ' | Sanitized: ' + str(res['sanitized_steam_cleaning_certified']))

if __name__ == '__main__':
    main()
