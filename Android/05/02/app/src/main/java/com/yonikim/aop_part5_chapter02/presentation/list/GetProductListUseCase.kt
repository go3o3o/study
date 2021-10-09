package com.yonikim.aop_part5_chapter02.presentation.list

import com.yonikim.aop_part5_chapter02.data.entity.product.ProductEntity
import com.yonikim.aop_part5_chapter02.data.repository.ProductRepository
import com.yonikim.aop_part5_chapter02.domain.UseCase

internal class GetProductListUseCase(
    private val productRepository: ProductRepository
): UseCase {

    suspend operator fun invoke(): List<ProductEntity> {
        return productRepository.getProductList()
    }
}