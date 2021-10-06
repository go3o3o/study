package com.yonikim.aop_part5_chapter02.data.repository

import com.yonikim.aop_part5_chapter02.data.entity.product.ProductEntity
import com.yonikim.aop_part5_chapter02.data.network.ProductApiService

class DefaultProductRepository(
    private val productApi: ProductApiService
): ProductRepository {
    override suspend fun getProductList(): List<ProductEntity> {
        TODO("Not yet implemented")
    }

    override suspend fun getLocalProductList(): List<ProductEntity> {
        TODO("Not yet implemented")
    }

    override suspend fun insertProductItem(productItem: ProductEntity): Long {
        TODO("Not yet implemented")
    }

    override suspend fun insertProductList(productList: List<ProductEntity>) {
        TODO("Not yet implemented")
    }

    override suspend fun updateProductItem(productItem: ProductEntity) {
        TODO("Not yet implemented")
    }

    override suspend fun getProductItem(itemId: Long): ProductEntity? {
        TODO("Not yet implemented")
    }

    override suspend fun deleteAll() {
        TODO("Not yet implemented")
    }

    override suspend fun deleteProductItem(itemId: Long) {
        TODO("Not yet implemented")
    }
}