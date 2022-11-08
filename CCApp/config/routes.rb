Rails.application.routes.draw do
  # resources :area_codes, only: [:show, :index]
  # resources :bill_codes
  resources :phase_codes, only: [:show, :index] do
    resources :bill_codes, only: [:show, :index]
  end

  resources :bill_codes, only: [:show, :index] do
    resources :area_codes, only: [:show, :index]
  end

  resources :area_codes, only: [:show, :index]
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
