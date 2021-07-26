const axios = require('axios')
const { v4: uuidv4 } = require('uuid')
const { sign } = require('jsonwebtoken')
const { encode: queryEncode } = require('querystring')

const config = require('../../lib/config')
const access_key = config.UPBIT_OPEN_API_ACCESS_KEY
const secret_key = config.UPBIT_OPEN_API_SECRET_KEY
const server_url = config.UPBIT_OPEN_API_SERVER_URL

module.exports.getAccounts = async () => {
  try {
    const payload = {
      access_key: access_key,
      nonce: uuidv4(),
    }
    const token = sign(payload, secret_key)

    const options = {
      method: 'GET',
      url: server_url + '/v1/accounts',
      headers: { Authorization: `Bearer ${token}` },
    }
    const result = await axios(options)

    return {
      status: 200,
      data: result.data,
    }
  } catch (err) {
    throw { status: err.status || 500, message: err.message }
  }
}

module.exports.getMarketAll = async () => {
  try {
    const options = {
      method: 'GET',
      url: server_url + '/v1/market/all?isDetails=true',
      headers: { Accept: 'application/json' },
    }
    const result = await axios(options)
    return {
      status: 200,
      data: result.data,
    }
  } catch (err) {
    throw { status: err.status || 500, message: err.message }
  }
}

module.exports.getOrdersChance = async ({ market }) => {
  try {
    const body = {
      market,
    }
    console.log(market)
    const query = queryEncode(body)
    const hash = crypto.createHash('sha512')
    const queryHash = hash.update(query, 'utf-8').digest('hex')

    const payload = {
      access_key: access_key,
      nonce: uuidv4(),
      query_hash: queryHash,
      query_hash_alg: 'SHA512',
    }
    const token = sign(payload, secret_key)

    const options = {
      method: 'GET',
      url: server_url + '/v1/orders/chance?' + query,
      headers: { Authorization: `Bearer ${token}` },
      json: body,
    }
    const result = await axios(options)
    return {
      status: 200,
      data: result.data,
    }
  } catch (err) {
    throw { status: err.status || 500, message: err.message }
  }
}

module.exports.getCandles = async () => {
  try {
    const options = {
      method: 'GET',
      url: server_url + '/v1/candles/minutes/1?market=KRW-BTC&count=1',
      headers: { Accept: 'application/json' },
    }
    const result = await axios(options)
    return {
      status: 200,
      data: result.data,
    }
  } catch (err) {
    throw { status: err.status || 500, message: err.message }
  }
}
