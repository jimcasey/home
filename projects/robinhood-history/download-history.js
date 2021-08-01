// Downloads Robinhood orders as a CSV
// -----------------------------------
// This was functional as of 2021-08-01, no guarantees it will continue to function should
// Robinhood tweak their browser app. 🤷‍♂️
//
// Instructions:
//  * Navigate to https://robinhood.com/account/history?type=orders in Chrome
//  * Keep scrolling to the bottom until all history has loaded
//  * Open the console (View > Developer > JavaScript Concole
//  * Copy+paste this script into the console and hit enter
//
// Should work when filtering transactions other than orders, although you should run through each
// filter type one at a time as different transaction types are not identified and it can get
// a little confusing.
//
// Original inspiration:
// https://anonovation.medium.com/how-to-download-your-robinhood-transaction-history-357b1ff4df15

;((fileName) => {
  const fields = new Set()
  transactions = []
  const addTransactionValue = (transaction, field, value) => {
    fields.add(field)
    transaction[field] = value
  }

  document.querySelectorAll('section').forEach((sectionElement) => {
    sectionElement
      .querySelectorAll(':scope > div')
      .forEach((transactionElement) => {
        const transaction = {}
        addTransactionValue(
          transaction,
          'Name',
          transactionElement.querySelector('h3').textContent,
        )
        transactionElement
          .querySelector('[data-testid=rh-ExpandableItem-content] .grid-3')
          .querySelectorAll('div')
          .forEach((fieldElement) => {
            valueElements = fieldElement.querySelectorAll('span > div')
            if (valueElements.length === 2) {
              addTransactionValue(
                transaction,
                valueElements[0].textContent,
                valueElements[1].textContent,
              )
            }
          })
        transactions.push(transaction)
      })
  })

  const csv = transactions
    .reduce(
      (lines, transaction) => [
        ...lines,
        fields
          .map((field) => {
            const value = transaction[field] || ''
            return value.includes(',') ? `"${value}"` : value
          })
          .join(','),
      ],
      [fields.join(',')],
    )
    .join('\n')
  const csvFile = new Blob([csv], { type: 'text/csv' })

  const anchor = document.createElement('a')
  anchor.href = URL.createObjectURL(csvFile)
  anchor.download = fileName
  anchor.click()
})('orders.csv')
