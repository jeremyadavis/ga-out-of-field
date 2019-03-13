import Link from 'next/link';
import fetch from 'isomorphic-unfetch';

import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';

import ExchangeRates from '../components/ExchangeRates';

const client = new ApolloClient({
  uri: 'https://48p1r2roz4.sse.codesandbox.io'
});

function Index(props) {
  return (
    <ApolloProvider client={client}>
      <div>
        Click{' '}
        <Link href="/about">
          <a>here</a>
        </Link>{' '}
        to read more
        <Link as={`/p/HowTo`} href="/post?title='How to do this thing'">
          <a>POST</a>
        </Link>
        <hr />
        <div>
          <h1>Batman TV Shows</h1>
          <ul>
            {props.shows.map(({ show }) => (
              <li key={show.id}>
                <Link as={`/p/${show.id}`} href={`/post?id=${show.id}`}>
                  <a>{show.name}</a>
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <ExchangeRates />
      </div>
    </ApolloProvider>
  );
}

Index.getInitialProps = async function() {
  const res = await fetch('https://api.tvmaze.com/search/shows?q=batman');
  const data = await res.json();

  console.log(`Show data fetched. Count: ${data.length}`);

  return {
    shows: data
  };
};

export default Index;
