<template>
  <v-container class="contenedor" fluid fill-height>
    <v-layout>
      <v-flex>
        <div class="msj_principal">
          <v-card class="mx-auto" color="#818181" dark>
            <v-card-title class="justify-center"> <span class="titulo">¡Bienvenido/a! Elige una liga para poder introducir los resultados del partido sobre el que quieras predecir el resultado</span></v-card-title>
          </v-card>
        </div>
        <div class="enlaces">
          <v-row>
            <router-link to="/bundesliga" tag="img" :src="require('@/assets/bundesliga.png')"></router-link>
            <router-link to="/laliga" tag="img" :src="require('@/assets/laliga.png')"></router-link> 
            <router-link to="/premierleague" tag="img" :src="require('@/assets/premierleague.png')"></router-link> 
            <router-link to="/seriea" tag="img" :src="require('@/assets/seriea.png')"></router-link> 
            <router-link to="/ligueone" tag="img" :src="require('@/assets/ligueone.png')"></router-link>
          </v-row>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {

}
</script>

<style>
.contenedor{
  background-image: url("https://images.unsplash.com/photo-1439736637365-748f240b24fb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjE3MzYxfQ&auto=format&fit=crop&w=1050&q=80");
  background-size: cover;
}

.titulo {
  color: white;
}

.msj_principal {
  margin-bottom: 100px;
}

.enlaces {
  margin-left: 125px;
  margin-right: auto;
}
</style>
