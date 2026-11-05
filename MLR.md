# Multiple Linear Regression

## 1. What Is Multiple Linear Regression?

Multiple Linear Regression (MLR) is a way to predict one number using several other numbers at the same time.

Think about guessing the price of a house. The size of the house matters, but so do the number of bedrooms, the age of the building, and how far it is from the city. If you looked at only one of these, your guess would be rough. MLR lets you look at all of them together and work out how much each one pushes the price up or down.

The thing we want to predict is called the **dependent variable** (or target). The things we use to predict it are called **independent variables** (or predictors). In the house example, price is the target, and size, bedrooms, age and distance are the predictors.

People use MLR because real life is rarely explained by a single factor. Sales depend on price *and* advertising *and* season. A student's marks depend on study hours *and* sleep *and* attendance. MLR gives us a simple, honest way to say: "Keeping everything else the same, here is what one factor does."

## 2. The Equation, Explained Simply

Every MLR model is built on one equation.&#32;

```latex
Y = b_0 + b_1 X_1 + b_2 X_2 + b_3 X_3 + \dots + b_n X_n + e
```

Here is what each part means:

- **Y** is the thing we want to predict (for example, house price).
- **X₁, X₂, X₃ … Xₙ** are the predictors (size, bedrooms, age, and so on).
- **b₀** is the *intercept*. It is the starting value of Y when every predictor is zero. Think of it as the "base" price before any feature is counted.
- **b₁, b₂, b₃ … bₙ** are the *coefficients*. Each one tells you how much Y changes when that one predictor goes up by 1, while the others stay the same.
- **e** is the *error*. No model is perfect, and this small leftover part covers everything the predictors cannot explain.

The coefficients are the heart of MLR. If the coefficient for size is 3,000, it means: "each extra square metre adds about 3,000 to the price, assuming the bedrooms, age and distance do not change."&#32;

**How does the model find the best numbers?** It uses a method called **Ordinary Least Squares (OLS)**. Imagine you draw a possible plane through your data. For every data point, measure how far the plane is from the real value (the error), square it, and add them all up. OLS simply picks the plane that makes this total as small as possible. In short: it finds the line (or plane) that misses the data points by the least amount overall. Software such as Excel, Python or R do this.

## 3. The Rules the Model Uses (Assumptions)

1. **Linearity.** The relationship between each predictor and the target should be roughly a straight line. If price rises slowly and then shoots up sharply with size, a straight line will not fit well.
2. **Independence.** Each data point should be separate from the others. One house's price should not be secretly tied to another's in the data (this is a common problem with data collected over time).
3. **Constant spread (homoscedasticity).** The errors should be about the same size everywhere. If your predictions are very close for cheap houses but wildly off for expensive ones, this rule is broken.
4. **Normal errors.** The leftover errors should form a bell-shaped pattern, with most being small and a few being large. This matters mostly for reliable tests and confidence ranges.
5. **No multicollinearity.** The predictors should not be near-copies of each other. If you include both "size in square feet" and "size in square metres," the model cannot tell which one deserves the credit.

**How do you check these?** The easiest way is to plot the errors (called *residuals*) after fitting the model. A healthy residual plot looks like a random cloud of dots with no pattern. If you see a curve, a funnel shape, or clear clusters, something is off. For multicollinearity, a number called the **VIF (Variance Inflation Factor)** helps: a value above about 5 to 10 is a warning sign.

## 4. A Worked Example: Predicting House Prices

Suppose a small study of houses in a town produced the model below. Prices are in lakh rupees.

```latex
\text{Price} = 8 + 0.06(\text{Area}) + 4(\text{Bedrooms}) - 0.5(\text{Age}) - 1.5(\text{Distance})
```

| Predictor | Coefficient | What it means in plain words |
| --- | --- | --- |
| Intercept | 8 | The base price before any feature is counted |
| Area (sq ft) | +0.06 | Each extra square foot adds 0.06 lakh (₹6,000) |
| Bedrooms | +4 | Each extra bedroom adds 4 lakh |
| Age (years) | −0.5 | Each extra year of age lowers the price by 0.5 lakh |
| Distance to city (km) | −1.5 | Each extra kilometre away lowers the price by 1.5 lakh |

Notice that area and bedrooms push the price up (positive signs), while age and distance pull it down (negative signs). The sign tells you the direction; the size tells you the strength.

**Making a prediction.** Take a house with 1,000 sq ft, 3 bedrooms, 10 years old, and 5 km from the city:

Price = 8 + 0.06(1000) + 4(3) − 0.5(10) − 1.5(5) = 8 + 60 + 12 − 5 − 7.5 = **67.5 lakh**

So the model predicts about ₹67.5 lakh. The real price will not match exactly, since the error term covers what the model cannot see, such as the view, the builder, or the street. Still, the prediction gives a solid starting point.

## 5. How Do We Know the Model Is Any Good?

Once a model is built, we need to check whether it is useful. A few simple measures do most of the work.

- **R² (R-squared)** tells you how much of the ups and downs in the target your predictors explain. It runs from 0 to 1. An R² of 0.80 means the model explains about 80% of the variation in price. Higher is generally better, but it is not the whole story.
- **Adjusted R²** is a fairer version. Plain R² always rises when you add more predictors, even useless ones (like the owner's shoe size). Adjusted R² only rises if the new predictor genuinely helps, so it protects you from over-stuffing the model.
- **p-values** test each predictor. A small p-value (commonly below 0.05) suggests the predictor really is related to the target and is not there by pure luck. A large p-value suggests it might be noise, and you could consider removing it.
- **RMSE (Root Mean Squared Error)** tells you, in the same units as your target, how far off your predictions typically are. If RMSE is 5 lakh, your guesses are usually within about 5 lakh of the truth.

A good habit is to test the model on data it has never seen. Split data into a *training set* (to build the model) and a *test set* (to check it). A model that does well on both has truly learned the pattern. A model that does well only on the training set has just memorised it, which is called **overfitting**.

**Two common traps to avoid:**

- **Multicollinearity:** predictors that overlap too much make the coefficients unstable and hard to trust.
- **Confusing correlation with cause:** MLR shows that factors move together, not that one *causes* the other. Ice cream sales and sunburns both rise in summer, but ice cream does not cause sunburn.

## 6. Strengths, Limits, Uses and Conclusion

**Where MLR is used.** It shows up almost everywhere: businesses forecast sales from price, advertising and season; hospitals study how age, weight and lifestyle affect blood pressure; farmers estimate crop yield from rainfall, soil and fertiliser; and schools look at how study habits affect exam scores.

| Strengths | Limitations |
| --- | --- |
| Easy to build and easy to explain | Assumes relationships are straight lines |
| Shows how much each factor matters | Sensitive to extreme values (outliers) |
| Works well with small to medium data | Struggles when predictors overlap heavily |
| Fast, and supported by almost every tool | Shows association, not proof of cause |
