class AreaCodesController < ApplicationController
  rescue_from ActiveRecord::RecordNotFound, with: :render_not_found_response

  
    def index
        if params[:bill_code_id]
            bill_code = BillCode.find(params[:bill_code_id])
            area_codes = bill_code.area_codes
        else
            area_codes = AreaCode.all
        end
    
        render json: area_codes, include: :bill_code
    end

    def show
        area_code = AreaCode.find(params[:id])
        render json: area_code, include: :bill_code
    end

    private

    def render_not_found_response
        render json: { error: "not found" }, status: :not_found
    end
end
