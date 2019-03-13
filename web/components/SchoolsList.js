import { Query } from 'react-apollo';
import gql from 'graphql-tag';
import { FlatList, ScrollView, Text, StyleSheet } from 'react-native';

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

      const schools = data.out_of_field.slice(0, 100);

      return (
        <ScrollView style={styles.scrollView}>
          <FlatList
            keyExtractor={item => item.index.toString()}
            data={schools}
            renderItem={({ item }) => (
              <Text>{`${item.district}, ${item.name}, ${
                item.outoffield_fte_pct
              }`}</Text>
            )}
          />
        </ScrollView>
      );
    }}
  </Query>
);

const styles = StyleSheet.create({
  scrollView: {
    backgroundColor: '#eeeeee',
    height: 300
  }
});

export default SchoolsList;
