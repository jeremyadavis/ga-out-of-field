import { Query } from 'react-apollo';
import gql from 'graphql-tag';

const SchoolsList = () => (
  <Query
    query={gql`
      {
        out_of_field {
          index
          district
          name
          lvl_3_desc
          fte
          outoffield_fte
          outoffield_fte_pct
        }
      }
    `}
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return data.out_of_field.map(
        ({ index, district, name, outoffield_fte_pct }) => (
          <div key={index}>
            <p>{`${district}, ${name}, ${outoffield_fte_pct}`}</p>
          </div>
        )
      );
    }}
  </Query>
);

export default SchoolsList;
