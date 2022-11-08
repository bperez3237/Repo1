class BillCode < ApplicationRecord
    belongs_to :phase_code
    has_many :area_codes
end
