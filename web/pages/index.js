import Link from 'next/link';
import fetch from 'isomorphic-unfetch';

import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';

import SchoolsList from '../components/SchoolsList';

import getConfig from 'next/config';
const { publicRuntimeConfig } = getConfig();

const client = new ApolloClient({
  uri: 'http://localhost:8080/v1alpha1/graphql',
  headers: {
    'x-hasura-admin-secret': publicRuntimeConfig.HASURA_GRAPHQL_ADMIN_SECRET
  }
});

function Index(props) {
  return (
    <ApolloProvider client={client}>
      <SchoolsList />
    </ApolloProvider>
  );
}

// Index.getInitialProps = async function() {
//   // const res = await fetch('https://api.tvmaze.com/search/shows?q=batman');
//   // const data = await res.json();

//   // console.log(`Show data fetched. Count: ${data.length}`);

//   return {
//     // shows: data
//   };
// };

export default Index;
