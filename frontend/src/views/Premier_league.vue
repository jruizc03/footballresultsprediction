<template>
        <v-container class="contenedor_premierleague" fluid fill-height>
          <v-layout>
            <v-flex>
                <div class="msj_principal">
                <v-card class="mx-auto" color="#818181" dark>
                  <v-card-title class="justify-center"> <span class="titulo">Elige los equipos e introduce las cuotas del partido. {{ resultado }}</span></v-card-title>
                </v-card>
                </div>
                <v-card class="mx-auto" color="#818181" dark>
                <v-form>
                <div class="eleccion">
                    <v-row align="center">
                        <v-col class="d-flex" cols="12" sm="6">
                            <v-select v-model="equipo_local" :items="items" label="Equipo Local" outlined></v-select>
                        </v-col>
                        <v-col class="d-flex" cols="12" sm="6">
                            <v-select v-model="equipo_visitante" :items="items" label="Equipo Visitante" outlined></v-select>
                        </v-col>
                    </v-row>
                  </div>
                  <div class="cuotas">
                    <v-container>
                      <v-row>
                        <v-text-field color="black" v-model="cuota_local" label="Cuota equipo local" outlined persistent-hint></v-text-field>
                        <v-spacer></v-spacer>
                        <v-text-field color="black" v-model="cuota_empate" label="Cuota empate" outlined persistent-hint></v-text-field>
                        <v-spacer></v-spacer>
                        <v-text-field color="black" v-model="cuota_visitante" label="Cuota equipo visitante" outlined persistent-hint></v-text-field>
                        <v-spacer></v-spacer>
                        <v-btn color="white" class="black--text" dark v-on:click=peticionPost()>Enviar</v-btn>
                    </v-row>
                    </v-container>
                  </div>
                </v-form>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </template>
      
<script>
import axios from 'axios'
export default {
    data: () => ({
    equipo_local: "",
    equipo_visitante: "",
    cuota_local: 1.0,
    cuota_empate: 1.0,
    cuota_visitante: 1.0,
    valor_equipo_local: 0,
    valor_equipo_visitante: 0,
    resultado: "",
    items: [
        'Manchester United' ,
        'Chelsea' ,
        'Manchester City' ,
        'Arsenal' ,
        'Tottenham' ,
        'Liverpool' ,
        'Everton' ,
        'Southampton' ,
        'Leicester' ,
        'Newcastle',
    ],
}),

methods: {
    peticionPost() {
      switch(this.equipo_local){
        case 'Manchester United':
        this.valor_equipo_local = 1;
        break;
        case 'Chelsea':
        this.valor_equipo_local = 2;
        break;
        case 'Manchester City':
        this.valor_equipo_local = 3;
        break;
        case 'Arsenal':
        this.valor_equipo_local = 4;
        break;
        case 'Tottenham':
        this.valor_equipo_local = 5;
        break;
        case 'Liverpool':
        this.valor_equipo_local = 6;
        break;
        case 'Everton':
        this.valor_equipo_local = 7;
        break;
        case 'Southampton':
        this.valor_equipo_local = 8;
        break;
        case 'Leicester':
        this.valor_equipo_local = 9;
        break;
        case 'Newcastle':
        this.valor_equipo_local = 10;
        break;
      }

      switch(this.equipo_visitante){
        case 'Manchester United':
        this.valor_equipo_visitante = 1;
        break;
        case 'Chelsea':
        this.valor_equipo_visitante = 2;
        break;
        case 'Manchester City':
        this.valor_equipo_visitante = 3;
        break;
        case 'Arsenal':
        this.valor_equipo_visitante = 4;
        break;
        case 'Tottenham':
        this.valor_equipo_visitante = 5;
        break;
        case 'Liverpool':
        this.valor_equipo_visitante = 6;
        break;
        case 'Everton':
        this.valor_equipo_visitante = 7;
        break;
        case 'Southampton':
        this.valor_equipo_visitante = 8;
        break;
        case 'Leicester':
        this.valor_equipo_visitante = 9;
        break;
        case 'Newcastle':
        this.valor_equipo_visitante = 10;
        break;
      }
      const path = 'http://localhost:5000/api/v1.0/prediccionpremierleague'
      axios.post(path, {
      equipo_local: this.valor_equipo_local,
      equipo_visitante: this.valor_equipo_visitante,
      cuota_local: this.cuota_local,
      cuota_empate: this.cuota_empate,
      cuota_visitante: this.cuota_visitante
    })
    .then(response => {
      this.resultado = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
    },
  },
}
</script>
      
<style>

.contenedor_premierleague {
background-image: url("https://wallpapercave.com/wp/wp1715673.jpg");
background-size: cover;
}

.cuotas {
margin-top: 25px;
margin-bottom: 100px;
}

</style>
      
      
      