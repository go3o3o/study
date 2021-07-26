const upbitService = require('../services/upbit')

module.exports.getAccounts = async (req, res) => {
  try {
    const result = await upbitService.getAccounts()

    res.status(result.status || 200).json(result.data)
  } catch (err) {
    return res.status(err.status).json(err.message)
  }
}

module.exports.getMarketAll = async (req, res) => {
  try {
    const result = await upbitService.getMarketAll()

    res.status(result.status || 200).json(result.data)
  } catch (err) {
    return res.status(err.status).json(err.message)
  }
}

module.exports.getOrdersChance = async (req, res) => {
  const params = req.body
  console.log(params)
  try {
    const result = await upbitService.getOrdersChance(params)

    res.status(result.status || 200).json(result.data)
  } catch (err) {
    return res.status(err.status).json(err.message)
  }
}

module.exports.getCandles = async (req, res) => {
  try {
    const result = await upbitService.getCandles()

    res.status(result.status || 200).json(result.data)
  } catch (err) {
    return res.status(err.status).json(err.message)
  }
}
