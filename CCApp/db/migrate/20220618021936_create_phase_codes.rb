class CreatePhaseCodes < ActiveRecord::Migration[7.0]
  def change
    create_table :phase_codes do |t|
      t.string :code
      t.string :name
      t.string :engineer
      t.string :uom

      t.timestamps
    end
  end
end
