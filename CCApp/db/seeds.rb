
require 'json'
file = File.open 'ccdb.json'
data = JSON.load file

puts "Start seeding"


data["codes"].each do |bill_code|

    pc = PhaseCode.find_or_create_by(
        code: bill_code["phase_code"],
        name: bill_code["name"],
        engineer: bill_code["engineer"],
        uom: bill_code["uom"]
    )

    bc = BillCode.create(
        code: bill_code["bill_code"],
        category: bill_code["category"],
        phase_code_id: pc.id,
        forecast_qty: bill_code["forecast_qty"],
        forecast_mhs: bill_code["forecast_mhs"],
        current_qty: bill_code["current_qty"],
        current_mhs: bill_code["current_mhs"],
        projected_forecast: bill_code["projected_forecast"],
        spent_to_date: bill_code["spent_to_date"],
        committed: bill_code["committed"]
    )

    if bill_code["areas"] != nil
        bill_code["areas"].each do |area_code|
            AreaCode.create(
                name: area_code["name"],
                eb_id: area_code["eb_id"],
                forecast_qty: area_code["forecast_qty"],
                forecast_mhs: area_code["forecast_mhs"],
                current_qty: area_code["current_qty"],
                current_mhs: area_code["current_mhs"],
                bill_code_id: bc.id
            )
        end
    end
end
     

puts "Done seeding"
