from parse_pdf import ChargeInfo

def calculate_overcharge(charges: ChargeInfo, expected_base_charge: float) -> float:
    return charges.base_charge - expected_base_charge + charges.extra_charges

if __name__ == "__main__":
    charges = ChargeInfo(base_charge=245.23, extra_charges=0)
    expected_base_charge = 245.23
    overcharge = calculate_overcharge(charges, expected_base_charge)
    print(f"Overcharge: ${overcharge:.2f}")