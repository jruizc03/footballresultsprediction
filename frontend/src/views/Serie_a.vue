<template>
    <v-container class="contenedor_seriea" fluid fill-height>
        <v-layout>
        <v-flex>
            <div class="msj_principal">
            <v-card class="mx-auto" color="#444644" dark max-width="525px">
                <v-card-title class="justify-center"> <span class="titulo">Elige los equipos e introduce las cuotas del partido.</span></v-card-title>
            </v-card>
            </div>
            <v-card class="mx-auto" color="#444644" dark>
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
              </v-card>
              <v-card class="mx-auto" color="#444644" dark>
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
            </v-card>

            <v-dialog v-model="dialog" width="600px">
                <v-card>
                  <v-card-title>
                    <span class="headline">{{ frase_final }}</span>
                  </v-card-title>
                  <v-card-text>Dicho resultado ha sido calculado para el partido {{ equipo_local }} vs {{ equipo_visitante }} que tenía como cuotas {{ cuota_local }} para el {{ equipo_local }}, {{ cuota_empate }} para el empate y {{ cuota_visitante }} para el {{ equipo_visitante }}.</v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="grey" text @click="dialog = false">Vale</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>

        </v-flex>
        </v-layout>
    </v-container>
</template>
      
<script>
import axios from 'axios'
export default {
    data: () => ({
      dialog: false,
      equipo_local: "",
      equipo_visitante: "",
      cuota_local: 1.0,
      cuota_empate: 1.0,
      cuota_visitante: 1.0,
      valor_equipo_local: 0,
      valor_equipo_visitante: 0,
      resultado: 0,
      frase_final: '',
    items: [
        'AC Milan' ,
        'Inter' ,
        'Napoli' ,
        'Lazio' ,
        'Roma' ,
        'Juventus' ,
        'Fiorentina' ,
        'Torino' ,
        'Udinese' ,
        'Parma',
    ],
}),

methods: {
    peticionPost() {
      switch(this.equipo_local){
        case 'AC Milan':
        this.valor_equipo_local = 1;
        break;
        case 'Inter':
        this.valor_equipo_local = 2;
        break;
        case 'Napoli':
        this.valor_equipo_local = 3;
        break;
        case 'Lazio':
        this.valor_equipo_local = 4;
        break;
        case 'Roma':
        this.valor_equipo_local = 5;
        break;
        case 'Juventus':
        this.valor_equipo_local = 6;
        break;
        case 'Fiorentina':
        this.valor_equipo_local = 7;
        break;
        case 'Torino':
        this.valor_equipo_local = 8;
        break;
        case 'Udinese':
        this.valor_equipo_local = 9;
        break;
        case 'Parma':
        this.valor_equipo_local = 10;
        break;
      }

      switch(this.equipo_visitante){
        case 'AC Milan':
        this.valor_equipo_visitante = 1;
        break;
        case 'Inter':
        this.valor_equipo_visitante = 2;
        break;
        case 'Napoli':
        this.valor_equipo_visitante = 3;
        break;
        case 'Lazio':
        this.valor_equipo_visitante = 4;
        break;
        case 'Roma':
        this.valor_equipo_visitante = 5;
        break;
        case 'Juventus':
        this.valor_equipo_visitante = 6;
        break;
        case 'Fiorentina':
        this.valor_equipo_visitante = 7;
        break;
        case 'Torino':
        this.valor_equipo_visitante = 8;
        break;
        case 'Udinese':
        this.valor_equipo_visitante = 9;
        break;
        case 'Parma':
        this.valor_equipo_visitante = 10;
        break;
      }
      const path = 'http://localhost:5000/api/v1.0/prediccionseriea'
      axios.post(path, {
      equipo_local: this.valor_equipo_local,
      equipo_visitante: this.valor_equipo_visitante,
      cuota_local: this.cuota_local,
      cuota_empate: this.cuota_empate,
      cuota_visitante: this.cuota_visitante
    })
    .then(response => {
      this.resultado = response.data
      if(this.resultado == 0){
        this.frase_final = "El ganador del encuentro será el " + this.equipo_local + "."
      }
      else if(this.resultado == 1){
        this.frase_final = "El encuentro terminará en empate."
      }
      else if(this.resultado == 2){
        this.frase_final = "El ganador del encuentro será el " + this.equipo_visitante + "."
      }
      this.dialog = true
    })
    .catch(e => {
      this.errors.push(e)
    })
    },
  },

}
</script>
      
<style>

.contenedor_seriea {
background-image: url("https://images.unsplash.com/photo-1510051640316-cee39563ddab?ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80");
background-size: cover;
}

.cuotas {
margin-top: 25px;
margin-bottom: 100px;
}

</style>
      
      
      