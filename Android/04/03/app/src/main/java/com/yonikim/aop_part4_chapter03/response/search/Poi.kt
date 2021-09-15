package com.yonikim.aop_part4_chapter03.response.search

data class Poi(
    val id: String? = null,
    val name: String? = null,
    val telNo: String? = null,
    val frontLat: Float? = null,
    val frontLon: Float? = null,
    val noorLat: Float,
    val noorLon: Float,
    val firstNo: String? = null,
    val secondNo: String? = null,
    val upperAddrName: String? = null,
    val middleAddrName: String? = null,
    val detailAddrName: String? = null,
    val lowerAddrName: String? = null,
    val detailBizName: String? = null,
    val rpFlag: String? = null,
    val parkFlag: String? = null,
    val detailInfoFlag: String? = null,
    val desc: String? = null,
)