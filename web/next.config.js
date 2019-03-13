const { parsed: localEnv } = require('dotenv').config({
  path: '../.env'
});
// const webpack = require('webpack');

// module.exports = {
//   webpack(config) {
//     config.plugins.push(new webpack.EnvironmentPlugin(localEnv));

//     return config;
//   }
// };

module.exports = {
  // serverRuntimeConfig: { // Will only be available on the server side
  //   mySecret: 'secret'
  // },
  publicRuntimeConfig: {
    // Will be available on both server and client
    HASURA_GRAPHQL_ADMIN_SECRET: process.env.HASURA_GRAPHQL_ADMIN_SECRET
  }
};
