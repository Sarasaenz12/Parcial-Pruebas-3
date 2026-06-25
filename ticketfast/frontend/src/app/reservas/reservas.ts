import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-reservas',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './reservas.html',
  styleUrl: './reservas.css'
})
export class ReservasComponent {
  email: string = '';
  zona: string = 'VIP';
  cantidad: number = 1;
  totalFormateado: string | null = null;

  private readonly API_URL = 'http://localhost:8001';

  constructor(private http: HttpClient) {}

  confirmarReserva(): void {
    const eventoId = 'frontend-evento-demo';

    const payload = {
      cliente_email: this.email,
      zona: this.zona,
      cantidad: Number(this.cantidad)
    };

    this.http.post(`${this.API_URL}/reservas/${eventoId}`, payload).subscribe({
      next: () => {
        this.http.get<any>(`${this.API_URL}/reservas/${eventoId}/resumen`).subscribe({
          next: (resumen) => {
            this.totalFormateado = this.formatearMoneda(resumen.total_recaudado);
          }
        });
      }
    });
  }

  private formatearMoneda(valor: number): string {
    return new Intl.NumberFormat('es-CO').format(valor);
  }
}