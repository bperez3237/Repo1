class PhaseCodesController < ApplicationController
    rescue_from ActiveRecord::RecordNotFound, with: :render_not_found_response
   
    def show
        phase_code = PhaseCode.find(params[:id])
        render json: phase_code, include: :bill_codes
    end

    def index
        phase_codes = PhaseCode.all
        render json: phase_codes, include: :bill_codes
    end

    private

    def render_not_found_response
        render json: { error: "not found" }, status: :not_found
    end
end



