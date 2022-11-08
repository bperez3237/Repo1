class CreateBillCodes < ActiveRecord::Migration[7.0]
  def change
    create_table :bill_codes do |t|
      t.string :code
      t.string :category
      t.integer :phase_code_id
      t.float :forecast_qty
      t.float :forecast_mhs
      t.float :current_qty
      t.float :current_mhs
      t.float :projected_forecast
      t.float :spent_to_date
      t.float :committed

      t.timestamps
    end
  end
end
