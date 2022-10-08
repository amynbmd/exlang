/* tslint:disable:no-unused-variable */

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { TestBed, async, inject } from '@angular/core/testing';
import { ItTransferStudentService } from './it-transfer-student.service';

describe('Service: ItTransferStudent', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ItTransferStudentService]
    });
  });

  it('should ...', inject([ItTransferStudentService], (service: ItTransferStudentService) => {
    expect(service).toBeTruthy();
  }));
});
