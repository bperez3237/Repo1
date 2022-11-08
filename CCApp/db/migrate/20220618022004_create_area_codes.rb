class CreateAreaCodes < ActiveRecord::Migration[7.0]
  def change
    create_table :area_codes do |t|
      t.string :name
      t.integer :eb_id
      t.float :forecast_qty
      t.float :forecast_mhs
      t.float :current_qty
      t.string :current_mhs
      t.integer :bill_code_id

      t.timestamps
    end
  end
end
