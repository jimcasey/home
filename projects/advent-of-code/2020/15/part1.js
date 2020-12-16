const INPUT = '14,8,16,0,1,17'
const TESTS = {
  '0,3,6': 436,
}

const ANSWER_POSITION = 2020

const findAnswer = (input) => {
  const nums = input.split(',').map(Number)
  for (let index = nums.length - 1; index < ANSWER_POSITION - 1; index++) {
    const lastIndex = nums.slice(0, nums.length - 1).lastIndexOf(nums[index])
		nums.push(lastIndex < 0 ? 0 : index - lastIndex)
  }
  return nums[nums.length - 1]
}

const run = async () => {
  const answer = findAnswer(INPUT)
  console.log(`The answer is ${answer}.`)
}

run()
