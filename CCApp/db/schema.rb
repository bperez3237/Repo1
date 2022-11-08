# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2022_06_18_022004) do
  create_table "area_codes", force: :cascade do |t|
    t.string "name"
    t.integer "eb_id"
    t.float "forecast_qty"
    t.float "forecast_mhs"
    t.float "current_qty"
    t.string "current_mhs"
    t.integer "bill_code_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "bill_codes", force: :cascade do |t|
    t.string "code"
    t.string "category"
    t.integer "phase_code_id"
    t.float "forecast_qty"
    t.float "forecast_mhs"
    t.float "current_qty"
    t.float "current_mhs"
    t.float "projected_forecast"
    t.float "spent_to_date"
    t.float "committed"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "phase_codes", force: :cascade do |t|
    t.string "code"
    t.string "name"
    t.string "engineer"
    t.string "uom"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
