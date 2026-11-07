import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity, ScrollView } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import Icon from 'react-native-vector-icons/MaterialIcons';

// Tela Inicial
function HomeScreen({ navigation }) {
    return (
        <ScrollView contentContainerStyle={styles.container}>
            <View style={styles.header}>
                <TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <Icon name="menu" size={30} color="#fff" />
                </TouchableOpacity>
                <Text style={styles.headerTitle}>Bem-vindo</Text>
            </View>

            {/* Espaço para a imagem personalizada */}
            <View style={styles.imageContainer}>
                <Image
                    source={require('./assets/placeholder.png')} // Substitua com sua imagem personalizada
                    style={styles.image}
                    resizeMode="cover"
                />
            </View>

            {/* Seção de Vocabulário */}
            <View style={styles.section}>
                <Text style={styles.sectionTitle}>Palavras do Dia</Text>
                <Text style={styles.word}>??kan - Um</Text>
                <Text style={styles.word}>Méjì - Dois</Text>
                <Text style={styles.word}>Métà - Três</Text>
            </View>

            {/* Botão para acessar Quiz */}
            <TouchableOpacity
                style={styles.quizButton}
                onPress={() => navigation.navigate('Quiz')}>
                <Text style={styles.quizButtonText}>Ir para Questões</Text>
            </TouchableOpacity>
        </ScrollView>
    );
}

// Tela de Quiz
function QuizScreen() {
    return (
        <View style={styles.container}>
            <Text style={styles.sectionTitle}>Quiz de Iorubá</Text>
            <Text style={styles.quizText}>Perguntas interativas aparecerão aqui.</Text>
        </View>
    );
}

// Configuração do Menu Lateral
const Drawer = createDrawerNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Drawer.Navigator initialRouteName="Home">
                <Drawer.Screen name="Início" component={HomeScreen} />
                <Drawer.Screen name="Quiz" component={QuizScreen} />
            </Drawer.Navigator>
        </NavigationContainer>
    );
}

// Estilos
const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        padding: 20,
    },
    header: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 20,
    },
    headerTitle: {
        fontSize: 24,
        color: '#fff',
        marginLeft: 10,
        backgroundColor: '#008753',
        padding: 10,
        borderRadius: 5,
    },
    imageContainer: {
        height: 200,
        marginBottom: 20,
    },
    image: {
        width: '100%',
        height: '100%',
        borderRadius: 10,
        backgroundColor: '#e0e0e0',
    },
    section: {
        marginBottom: 20,
    },
    sectionTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#008753',
        marginBottom: 10,
    },
    word: {
        fontSize: 16,
        marginBottom: 5,
    },
    quizButton: {
        backgroundColor: '#008753',
        padding: 15,
        borderRadius: 5,
        alignItems: 'center',
    },
    quizButtonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    },
    quizText: {
        fontSize: 16,
        color: '#333',
        marginTop: 20,
    },
});
