def profit(x):
        profitPerItem = x["sell_price"]-x["cost_price"]
        profitTotal = profitPerItem * x["inventory"]
        profitTotalRounded = round(profitTotal, 2)
        profitTotalRounded = profitTotalRounded
        return profitTotalRounded
