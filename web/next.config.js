const { parsed: localEnv } = require('dotenv').config({
  path: '../.env'
});

module.exports = {
  // serverRuntimeConfig: { // Will only be available on the server side
  //   mySecret: 'secret'
  // },
  publicRuntimeConfig: {
    // Will be available on both server and client
    HASURA_GRAPHQL_ADMIN_SECRET: process.env.HASURA_GRAPHQL_ADMIN_SECRET
  },
  webpack: config => {
    // Alias all `react-native` imports to `react-native-web`
    config.resolve.alias = {
      ...(config.resolve.alias || {}),
      'react-native$': 'react-native-web'
    };

    return config;
  }
};
