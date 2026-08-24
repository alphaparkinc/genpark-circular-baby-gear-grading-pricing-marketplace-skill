class CircularBabyGearGradingPricingMarketplaceClient:
    def grade_and_value_baby_gear(self, gear_model='Uppababy Vista V2 Stroller', original_retail_cad=1299.0, condition='open_box'):
        rev_resale_value = round(original_retail_cad * 0.68, 2)
        return {
            'item_valuation_id': 'rev_val_8812',
            'gear_model': gear_model,
            'algorithmic_condition_grade': 'CERTIFIED_OPEN_BOX_PRISTINE',
            'rev_algorithm_resale_cad': rev_resale_value,
            'parent_savings_pct': 32.0,
            'safety_recall_registry_cleared': True,
            'sanitized_steam_cleaning_certified': True,
            'instant_payout_offer_cad': round(rev_resale_value * 0.75, 2)
        }
