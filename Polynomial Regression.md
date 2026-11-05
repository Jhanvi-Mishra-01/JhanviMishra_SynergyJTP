# Polynomial Regression

## 1. What Is Polynomial Regression?

Polynomial regression is a way to predict a number when the pattern in your data is a curve, not a straight line.

Imagine you track how fast a car uses fuel at different speeds. At very low speeds it wastes fuel, at moderate speeds it is efficient, and at high speeds it wastes fuel again. If you draw this, you get a U-shaped curve. A straight line would cut right through the middle and describe the pattern badly. Polynomial regression fixes this by letting the line bend.

It still uses the same machinery underneath, but it adds extra "curved" terms (like X squared and X cubed) so the fitted line can bend to follow the data.

The thing we predict is the **dependent variable** (or target), and the thing we use to predict it is the **independent variable** (or predictor). In the fuel example, fuel use is the target and speed is the predictor.

## 2. The Equation

The polynomial regression equation looks like this:

```latex
Y = b_0 + b_1 X + b_2 X^2 + b_3 X^3 + \dots + b_n X^n + e
```

Here is what each part means:

- **Y** is the thing we want to predict.
- **X** is the predictor. **X², X³ …** are simply X multiplied by itself two times, three times, and so on. These extra terms are what let the line curve.
- **b₀** is the *intercept*, the starting value of Y when X is zero.
- **b₁, b₂, b₃ … bₙ** are the *coefficients*. Each one controls how strongly its term shapes the curve.
- **e** is the *error*, the small leftover that the model cannot explain.
- **n** is the *degree* of the polynomial, meaning the highest power of X used.

The degree decides how much the curve can bend:

| Degree | Name | Shape it can make |
| --- | --- | --- |
| 1 | Linear | A straight line |
| 2 | Quadratic | One bend, like a U or an upside-down U |
| 3 | Cubic | Up to two bends, like an S |
| 4 and above | Higher degree | More wiggles, with more risk of overfitting |

Here is a nice surprise: although the curve bends, this is still called a *linear* model. That is because the equation is linear in the coefficients (the b values). We just treat X, X² and X³ as separate input columns and run ordinary linear regression on them. In other words, polynomial regression is multiple linear regression in disguise. The model finds the best coefficients using Ordinary Least Squares, which picks the curve that misses the data points by the smallest total amount.

## 3. Choosing the Degree: Not Too Little, Not Too Much

The biggest decision in polynomial regression is picking the degree.&#32;

- **Too stiff (underfitting).** A degree that is too low, like a straight line through curved data, misses the real pattern. The model is too simple, and its predictions are poor on both old and new data.
- **Just right (good fit).** A sensible degree follows the true shape of the data without chasing every little bump. This gives good predictions on new data too.
- **Too bendy (overfitting).** A degree that is too high makes the curve wiggle to touch every single point. It looks perfect on the data you already have, but it has memorised the random noise. On new data it performs badly and can swing wildly, especially at the edges.

A handy rule of thumb: **start low and go up only if you need to.** Try degree 2 first. Move to 3 only if the fit clearly improves. In most real projects, degrees above 3 or 4 are rarely a good idea.

**How to pick the degree sensibly:**

1. Plot your data first and look at it. Count the bends you can see, because a curve with one bend usually needs degree 2.
2. Fit several degrees (for example 1, 2, 3, 4).
3. Compare them on data the model has not seen, using a *test set* or *cross-validation*.
4. Choose the simplest degree that performs well. If two models do about equally well, pick the simpler one.

## 4. A Worked Example: Predicting Plant Height

Suppose a student measures a plant's height every week. The plant grows quickly at first, then slows down. A quadratic (degree 2) model fits this well.&#32;

```latex
\text{Height (cm)} = 1 + 4(\text{Week}) - 0.2(\text{Week}^2)
```

| Term | Coefficient | What it means in plain words |
| --- | --- | --- |
| Intercept | 1 | The plant starts at about 1 cm |
| Week | +4 | Pushes height up, giving fast early growth |
| Week² | −0.2 | Pulls the curve down, so growth slows over time |

The positive Week term and the negative Week² term work against each other. Early on, Week dominates and the plant shoots up. Later, the Week² term grows larger and slows the climb. That tug-of-war is what creates the bend.

**Making predictions.** Put different weeks into the equation:

| Week | Calculation | Predicted height (cm) |
| --- | --- | --- |
| 0 | 1 + 0 − 0 | 1.0 |
| 2 | 1 + 8 − 0.8 | 8.2 |
| 5 | 1 + 20 − 5 | 16.0 |
| 10 | 1 + 40 − 20 | 21.0 |
| 15 | 1 + 60 − 45 | 16.0 |

Notice how the plant gains about 7 cm in the first two weeks, but only about 5 cm over the five weeks from week 5 to week 10. The growth is clearly slowing, which a straight line could never show.

The model peaks at week 10 (21 cm) and then predicts the plant will shrink. In real life, a plant would more likely just stop growing. This is why you should only trust a polynomial model inside the range of data it was built on.

## 5. How Do We Know the Model Is Any Good?

Once the curve is fitted, a few simple checks tell you whether it can be trusted.

- **R² (R-squared)** shows how much of the ups and downs in the target the curve explains, on a scale from 0 to 1. An R² of 0.90 means the model explains about 90% of the variation.
- **Adjusted R²** is a fairer version. Plain R² always rises when you raise the degree, even if the extra bend is useless. Adjusted R² only rises when the new term truly helps.
- **RMSE (Root Mean Squared Error)** tells you, in the same units as your target, how far off the predictions typically are. If RMSE is 1.5 cm, your plant-height guesses are usually within about 1.5 cm.
- **Residual plot.** Plot the leftover errors. A healthy plot looks like a random cloud. If you still see a curve, the model is too simple. If errors fan out, the spread is uneven.

The most important check is to test the model on data it has never seen. Split your data into a *training set* and a *test set*. A model that scores well on training but poorly on test is overfitting.

**Common traps to avoid:**

- **Going too high in degree.** More bends always look better on the data you have, but they usually hurt on new data.
- **Predicting outside the data range.** Polynomial curves can shoot off to extreme values just beyond the edges, as the plant example showed.
- **Big numbers causing trouble.** X³ or X⁴ can become huge. Scaling or centring X (for example, subtracting its average) keeps the maths stable and also reduces overlap between the terms.
- **Outliers.** One extreme point can drag a flexible curve far away from the real trend.

## 6. Strengths, Limits, Uses and Conclusion

**Where polynomial regression is used.** It helps wherever the pattern bends: studying how crop yield changes with fertiliser (more helps, then too much hurts), tracking the growth of a population or a plant, modelling how temperature relates to energy use, understanding how a drug dose affects the body, and predicting how a product's sales rise and fall across a season.

| Strengths | Limitations |
| --- | --- |
| Captures curved patterns a straight line misses | Easy to overfit if the degree is too high |
| Simple to understand and build | Unreliable when predicting beyond the data range |
| Uses the same tools as linear regression | Sensitive to outliers |
| Flexible with just one extra setting (degree) | Coefficients are harder to explain than in a straight line |
