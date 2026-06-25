import { Routes } from '@angular/router';
import { ReservasComponent } from './reservas/reservas';

export const routes: Routes = [
  { path: 'reservas', component: ReservasComponent },
  { path: '', redirectTo: 'reservas', pathMatch: 'full' },
];