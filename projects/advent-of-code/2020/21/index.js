const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // mxmxvkd,sqjhc,fvjkl
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const parseFood = (input) => {
  const [_, ingredients, allergens] = input.match(
    /(^[a-z ]+) \(contains ([a-z, ]+)\)$/,
  )
  return [ingredients.split(' '), allergens.split(', ')]
}

const run = async () => {
  const input = await readInput()
  let foods = input.map(parseFood)

  const ingredientAllergens = {}
  foods.forEach(([ingredients, allergens]) =>
    ingredients.forEach((ingredient) => {
      const arr = ingredientAllergens[ingredient] || []
      ingredientAllergens[ingredient] = [...arr, ...allergens].filter(
        (value, index, arr) => arr.indexOf(value) === index,
      )
    }),
  )

  foods.forEach(([ingredients, allergens]) =>
    Object.entries(ingredientAllergens).forEach(([ingredient, map]) => {
      if (!ingredients.includes(ingredient)) {
        ingredientAllergens[ingredient] = map.filter(
          (allergen) => !allergens.includes(allergen),
        )
      }
    }),
  )

  const possibleAllergens = Object.keys(ingredientAllergens)
    .filter((ingredient) => !!ingredientAllergens[ingredient].length)
    .reduce(
      (obj, ingredient) => ({
        ...obj,
        [ingredient]: ingredientAllergens[ingredient],
      }),
      {},
    )

  const reducedIngredients = []
  while (
    (reduced = Object.entries(possibleAllergens).find(
      ([ingredient, allergens]) =>
        allergens.length === 1 && !reducedIngredients.includes(ingredient),
    ))
  ) {
    const [reduceIngredient, [reduceAllergen]] = reduced
    reducedIngredients.push(reduceIngredient)

    Object.entries(possibleAllergens).forEach(([ingredient, allergens]) => {
      if (ingredient === reduceIngredient) return
      possibleAllergens[ingredient] = allergens.filter(
        (allergen) => allergen !== reduceAllergen,
      )
    })
  }

  const allergenIngredients = Object.entries(possibleAllergens).reduce(
    (obj, [ingredient, [allergen]]) => ({ ...obj, [allergen]: ingredient }),
    {},
  )

  const answer = Object.keys(allergenIngredients)
    .sort()
    .map((allergen) => allergenIngredients[allergen])
    .join(',')

  console.log('List of ingredients sorted by their allergen:')
  console.log(answer)
}

run()
