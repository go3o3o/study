'use strict'
const SwaggerExpress = require('swagger-express-mw')
const SwaggerTools = require('swagger-tools')
const express = require('express')

const app = express()

const options = {
  controllers: './api/controllers',
  useStubs: process.env.NODE_ENV === 'development' ? true : false, // Conditionally turn on stubs (mock mode)
}

var config = {
  appRoot: __dirname, // required config
}

SwaggerExpress.create(config, function (err, swaggerExpress) {
  if (err) {
    throw err
  }

  // install middleware
  swaggerExpress.register(app)

  let swaggerObjectLoaded = swaggerExpress.runner.swagger
  SwaggerTools.initializeMiddleware(swaggerObjectLoaded, function (middleware, err) {
    if (err) {
      logger.error(err)
      throw err
    }
    app.disable('etag')
    app.use(middleware.swaggerMetadata())
    app.use(middleware.swaggerValidator())
    app.use(middleware.swaggerRouter(options))

    app.use(middleware.swaggerUi())
    app.get('/', async (req, res) => {
      try {
        res.status(200).redirect('/docs/#/')
      } catch (e) {
        logger.error(e)
        res.status(500).send()
      }
    })

    app.use((req, res, next) => {
      console.error(`Error 404 on ${req.url}.`)
      res.status(404).send({ status: 404, error: 'Not found' })
    })
  })

  var port = process.env.PORT || 10010
  app.listen(port)
})
module.exports = app
