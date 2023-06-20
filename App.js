import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { TailwindProvider } from 'tailwindcss-react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './screens/HomeScreen';
import RestaurantScreen from './screens/RestaurantScreen';
import CategoriesScreen from './screens/CategoriesScreen';
import CitiesScreen from './screens/CitiesScreen';

//sanity deploy, depois do cd y
// sanity start cd y

const Stack = createNativeStackNavigator();


export default function App() {
  return (
    <NavigationContainer>
      <TailwindProvider>
        <Stack.Navigator>
          <Stack.Screen name="Home" component={HomeScreen}/>
          <Stack.Screen name="City" component={CitiesScreen}/>
          <Stack.Screen name="Restaurant" component={RestaurantScreen}/>
          <Stack.Screen name="Categories" component={CategoriesScreen}/>
        </Stack.Navigator>
      </TailwindProvider>
    </NavigationContainer>
  );
}

