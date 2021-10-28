package com.yonikim.aop_part5_chapter05.presenter

interface BaseView<PresenterT: BasePresenter> {

    val presenter: PresenterT
}