export const random: {
  (max: number): number
  (min: number, max: number): number
} = (...args) => {
  const max = args[args.length - 1]
  const min = args.length === 1 ? 0 : args[0]

  return min + Math.floor(Math.random() * Math.floor(max - min))
}
