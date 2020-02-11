class ArticlesController < ApplicationController

  before_action :set_article, only: [:edit, :update, :show, :destroy]

  def new
    @article = Article.new
  end

  def edit
  end

  def update
    if @article.update(article_params)
      flash[:notice] = "Article was successfully updated"
      redirect_to articles_path(@article)
    else
      render 'edit'
    end
  end


  def create
    @article = Article.new(article_params)
    if @article.save
      flash[:notice] = "Article was successfully created"
      redirect_to articles_path(@article)
    else
      render 'new'
    end
  end

  def destroy
    @article.destroy
    flash[:notice] = "The article has been deleted"
    redirect_to articles_path
  end

  def index
    @articles = Article.all
  end

  def show
  end


  private

  def set_article
    @article = Article.find(params[:id])
  end
  
  def article_params
    params.require(:article).permit(:title, :description)
  end


end