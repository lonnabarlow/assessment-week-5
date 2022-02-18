const Sequalize = require('sequelize')
require('dotenv').config()

const sequelize = new Sequalize(process.env.CONNECTION_STRING, {
    dialect: 'postgres',
    dialectOptions: {
        ssl: {
            rejectUnauthorized: false
        }
    }
})
