package com.example.weathervisionapp.data.model

import androidx.compose.ui.graphics.Color

data class AirQuality(
    val percentage: Float,
    val color: Color,
    val description: String
)