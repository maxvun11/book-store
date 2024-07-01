import React from 'react';
import {StyleSheet} from 'react-native';
import {Component} from 'react/cjs/react.production.min';
import {NavigationContainer} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import HomeScreen from './Assignment/Screens/HomeScreen';
import ViewScreen from './Assignment/Screens/ViewScreen';
import BookScreen from './Assignment/Screens/BookScreen';
import ViewBorrowBook from './Assignment/Screens/ViewBorrowBook';
import SearchScreen from './Assignment/Screens/SearchScreen';
import RateUsScreen from './Assignment/Screens/RateUsScreen';
import ReviewBookScreen from './Assignment/Screens/ReviewBookScreen';
import BorrowedBookScreen from './Assignment/Screens/BorrowedBookScreen';
import SearchAllScreen from './Assignment/Screens/SearchAllScreen';
import ViewSearchAllScreen from './Assignment/Screens/ViewSearchAllScreen';
import PhysicalViewScreen from './Assignment/Screens/PhysicalViewBook';

const Stack = createStackNavigator();
export default class App extends Component {
  render() {
    return (
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen
            name="HomeScreen"
            component={HomeScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="ViewScreen"
            component={ViewScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="BookScreen"
            component={BookScreen}
            options={styles.HeaderOptionsStyle}
          />
          
          <Stack.Screen
            name="BorrowedBookScreen"
            component={BorrowedBookScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="ViewBorrowBook"
            component={ViewBorrowBook}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="SearchScreen"
            component={SearchScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="RateUsScreen"
            component={RateUsScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="ReviewBookScreen"
            component={ReviewBookScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="SearchAllScreen"
            component={SearchAllScreen}
            options={styles.HeaderOptionsStyle}
          />
          <Stack.Screen
            name="ViewSearchAllScreen"
            component={ViewSearchAllScreen}
            options={styles.HeaderOptionsStyle}
          />
          
          <Stack.Screen
            name="PhysicalViewScreen"
            component={PhysicalViewScreen}
            options={styles.HeaderOptionsStyle}
          />
        
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
}
const styles = StyleSheet.create({
  HeaderOptionsStyle: {
    headerStyle: {
      backgroundColor: '#a80000',
    },
    headerTintColor: '#fff',
    headerTitleStyle: {
      fontWeight: 'bold',
    },
  },
});