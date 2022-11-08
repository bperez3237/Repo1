class BillCodesController < ApplicationController
    rescue_from ActiveRecord::RecordNotFound, with: :render_not_found_response

    def index
        if params[:phase_code_id]
            phase_code = PhaseCode.find(params[:phase_code_id])
            bill_codes = phase_code.bill_codes
        else
            bill_codes = BillCode.all
        end

        render json: bill_codes, include: :area_codes
    end

    def show
        bill_code = BillCode.find(params[:id])
        render json: bill_code, include: :area_codes
    end

    private

    def render_not_found_response
        render json: { error: "not found" }, status: :not_found
    end

end

