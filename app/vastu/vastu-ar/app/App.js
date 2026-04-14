import React, { useEffect, useState } from 'react';
import { Text, View } from 'react-native';
import { Magnetometer } from 'expo-sensors';

export default function App() {
  const [heading, setHeading] = useState(0);

  useEffect(() => {
    const subscription = Magnetometer.addListener(data => {
      let angle = Math.atan2(data.y, data.x) * (180 / Math.PI);
      if (angle < 0) angle += 360;
      setHeading(Math.round(angle));
    });

    return () => subscription.remove();
  }, []);

  const getDirection = (angle) => {
    if (angle >= 45 && angle < 135) return "East";
    if (angle >= 135 && angle < 225) return "South";
    if (angle >= 225 && angle < 315) return "West";
    return "North";
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Heading: {heading}°</Text>
      <Text>Direction: {getDirection(heading)}</Text>
    </View>
  );
}