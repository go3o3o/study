package com.yonikim.aop_part5_chapter02.presentation.profile

import android.net.Uri
import com.yonikim.aop_part5_chapter02.data.entity.product.ProductEntity
import com.yonikim.aop_part5_chapter02.presentation.list.ProductListState

sealed class ProfileState {
    object UnInitialized : ProfileState()

    object Loading : ProfileState()

    data class Login(
        val idToken: String
    ) : ProfileState()

    sealed class Success: ProfileState() {
        data class Registered(
            val userName: String,
            val profileImageUri: Uri?,
            val productList: List<ProductEntity> = listOf()
        ): Success()

        object NotRegistered: Success()
    }

    object Error : ProfileState()
}