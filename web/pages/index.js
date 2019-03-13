// import App from '../components/App';
// import Header from '../components/Header';
import SchoolsList from '../components/SchoolsList';
import { StyleSheet, Text, View } from 'react-native';

function Index(props) {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Georgia Out Of Field</Text>

      <SchoolsList />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    flexGrow: 1,
    justifyContent: 'center'
  },
  text: {
    alignItems: 'center',
    fontSize: 24,
    color: 'red'
  }
});

export default Index;
