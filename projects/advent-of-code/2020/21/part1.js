const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 5
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

const appendUnique = (map, key, arr) =>
  (map[key] = [...(map[key] || []), ...arr].filter(
    (value, index, arr) => arr.indexOf(value) === index,
  ))

const run = async () => {
  const input = await readInput()
  let foods = input.map(parseFood)

  const ingredientAllergens = {}
  foods.forEach(([ingredients, allergens]) =>
    ingredients.forEach((ingredient) =>
      appendUnique(ingredientAllergens, ingredient, allergens),
    ),
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

  const safeIngredients = Object.keys(ingredientAllergens).filter(
    (ingredient) => !ingredientAllergens[ingredient].length,
  )

  const answer = foods.reduce(
    (count, [ingredients]) =>
      count +
      ingredients.filter((ingredient) => safeIngredients.includes(ingredient))
        .length,
    0,
  )

  console.log(`Safe ingredients are included ${answer} times.`)
}

run()
